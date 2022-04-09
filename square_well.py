# packages
import numpy as np
from matplotlib import pyplot as plt, animation
from PIL import Image
from sklearn.preprocessing import normalize
import sys

image_name = sys.argv[1]
image = Image.open(image_name)
size = image.size

img_array = np.flipud(np.array(image)[:,:,0])

img_x = len(img_array[:,0])
img_y = len(img_array[0,:])

# reformat non-square images
if img_x < img_y:
    img_array = img_array[:,:img_x]
else:
    img_array = img_array[:img_y,:]

img_array = normalize(img_array,axis=1,norm='l1')

psi0 = img_array

class Wavefunction:
    def __init__(self, psi0):
        self.psi = psi0

        self.Lx, self.Ly = self.psi.shape

        self.x = np.linspace(0,self.Lx,self.Lx)
        self.y = np.linspace(0,self.Ly,self.Ly)

        self.xx, self.yy = np.meshgrid(self.x,self.y)

        self.klin_x = 2.0 * np.pi / self.Lx * np.arange(-self.Lx/2,self.Lx/2)
        self.klin_y = 2.0 * np.pi / self.Ly * np.arange(-self.Ly/2,self.Ly/2)

        self.kx, self.ky = np.meshgrid(self.klin_x,self.klin_y)

        self.kx = np.fft.ifftshift(self.kx)
        self.ky = np.fft.ifftshift(self.ky)

        self.kSq = self.kx**2 +self.ky**2

        self.G = 40

        self.dt = 1.5

        # square well / empty potential
        self.V = self.psi*0;

        self.t = 0

    def evolve(self):
        # 1/2 step
        self.psi = np.exp(-1.j*self.dt/2.0*self.V) * self.psi

        #drift
        self.psihat = np.fft.fftn(self.psi)
        self.psihat = np.exp(self.dt * (-1.j*self.kSq/2.)) * self.psihat
        self.psi = np.fft.ifftn(self.psihat)

        # 1/2 kick
        self.psi = np.exp(-1.j*self.dt/2.0*self.V) * self.psi

        # update time
        self.t += self.dt

    def rho(self):
        return np.abs(self.psi)**2

psi = Wavefunction(psi0)

fig, ax = plt.subplots()
psi_ax = plt.pcolormesh(psi.rho(), cmap='inferno')


def animate(i):
    psi_ax.set_array(psi.rho())
    plt.title(r"$\rho = |\psi|^{2}$")
    psi.evolve()

filename = sys.argv[1].split(".")[0] + ".mp4"
anim = animation.FuncAnimation(fig, animate, interval = 50, frames = 250)
anim.save(filename)
