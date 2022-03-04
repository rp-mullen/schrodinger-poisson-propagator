# packages
import numpy as np
from matplotlib import pyplot as plt, animation
from PIL import Image
from scipy.integrate import trapz
from scipy import fftpack
from sklearn.preprocessing import normalize

# load image from command line
#image_name = input("Image to load: ")
image_name = "chimp.jpeg"
image = Image.open(image_name)
#orig_size = image.size
#image = image.transform(orig_size, Image.EXTENT, (0,0, 500, 500))

img_array = np.flipud(np.array(image)[:,:,0])
img_array = normalize(img_array,axis=1,norm='l1')

# define normalized 2D gaussian
def gaus2d(x=0, y=0, mx=0, my=0, sx=1, sy=1):
    return 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))

x = np.linspace(-5, 5)
y = np.linspace(-5, 5)
x, y = np.meshgrid(x, y) # get 2D variables instead of 1D
z = gaus2d(x, y)

# physical parameters
#-------------------------------------------------------------------------------
#psi0 = img_array
psi0 = z

Lx = len(psi0[:,0])
Ly = len(psi0[0,:])

x= np.linspace(0,Lx,Lx)
y = np.linspace(0,Ly,Ly)

k0_y = -0.5
k0_x = -0.5

kx = k0_x + np.arange(Lx)/Lx
ky = k0_y + np.arange(Ly)/Ly

hbar = 1
m = 1

# Schrodinger Evolution Class
#-------------------------------------------------------------------------------
class Evolver:
    def __init__(self, x,y, psi_0, V, k0=0.00,m=1):
        self.x = x
        self.y = y


        self.dx = x[1] - x[0]
        self.dy = y[1] - y[0]


        self.Lx = len(x)
        self.Ly = len(y)

        self.k0 = k0
        self.kx = self.k0 + 2 * np.pi * self.Lx * np.arange(self.Lx)
        self.ky = self.k0 + 2 * np.pi * self.Ly * np.arange(self.Ly)

        self.xp, self.yp = np.meshgrid(self.x,self.y)
        self.kxp, self.kyp = np.meshgrid(self.kx, self.ky)

        self.psi_xy = psi_0
        self.psi_k = None

        self.dt = 1.0e-8

        self.V = V

        self.xy_evolve_half = None
        self.xy_evolve = None
        self.k_evolve = None

    def psi_xy_half(self):
        self.psi_xy = self.psi_xy * np.exp(-1j * self.dt * self.V * 0.5) * np.exp(1j* self.k0 *
            self.xp) * np.exp(1j * self.k0 * self.yp)

    def phi_from_psi(self):
        self.psi_k = fftpack.fft(self.psi_xy)

    def phi_fullstep(self):
        self.psi_k = self.psi_k * np.exp(-1j * (self.kxp**2 + self.kyp**2) * self.dt * 0.5)

    def psi_from_phi(self):
        self.psi_xy = fftpack.ifft(self.psi_k)


    def evolve(self):
        self.psi_xy_half()
        self.phi_from_psi()
        self.phi_fullstep()
        self.psi_from_phi()
        self.psi_xy_half()

# Potential Generator
#-------------------------------------------------------------------------------
def gen_V(Lx,Ly):
    V = np.zeros((Lx,Ly))
    V[0][:] = 1
    return V
#-------------------------------------------------------------------------------
V = gen_V(Lx,Ly)

evo = Evolver(x,y,psi0,V)
evo.evolve()

fig, ax = plt.subplots()
psi_ax = plt.pcolormesh(np.sqrt(evo.psi_xy.real**2 + evo.psi_xy.imag**2),cmap='jet')

# Animation
#-------------------------------------------------------------------------------
def animate(i):
    psi_ax.set_array(np.sqrt(evo.psi_xy.real**2 + evo.psi_xy.imag**2))
    evo.evolve()

anim = animation.FuncAnimation(fig, animate, interval = 100, frames = 25)
anim.save("chimp.mp4")
plt.show()
