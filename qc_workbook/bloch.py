import numpy as np
import matplotlib.pyplot as plt

def make_sphere():
    fig = plt.figure()
    ax = fig.add_axes([0., 0., 0.98, 1.], projection='3d')
    ax.set_axis_off()
    ax.set_box_aspect((1., 1., 0.9), zoom=1.6)
    ax.set(xlim=(-1., 1.), ylim=(-1., 1.), zlim=(-1., 1.),
           xticks=[], yticks=[], zticks=[])

    ax.text(0.95, -0.3, 0., 'X', fontsize=16., color='gray')
    ax.text(0.1, 0.95, 0., 'Y', fontsize=16., color='gray')
    ax.text(0.1, 0., 0.95, 'Z', fontsize=16., color='gray')

    twopi = np.pi * 2.
    theta, phi = np.mgrid[0.:np.pi:21j, 0.:twopi:41j]
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    ax.plot_surface(x, y, z, color='#aaaaaa', alpha=0.1, shade=True)

    phi = np.linspace(0., twopi, 41)
    ax.plot(np.cos(phi), np.sin(phi), np.zeros_like(phi), color='gray', alpha=0.1, linestyle='--')

    ax.quiver(0., 0., 0., 1., 0., 0., length=1., color='gray', alpha=0.4, arrow_length_ratio=0.1)
    ax.quiver(0., 0., 0., 0., 1., 0., length=1., color='gray', alpha=0.4, arrow_length_ratio=0.1)
    ax.quiver(0., 0., 0., 0., 0., 1., length=1., color='gray', alpha=0.4, arrow_length_ratio=0.1)

    cax = fig.add_axes([0.98, 0., 0.02, 1.])

    return fig


def draw_path(x, y, z, t):
    fig = make_sphere()

    fig.axes[0].plot(x, y, z, linewidth=0.2, color='gray')
    pc = fig.axes[0].scatter(x, y, z, s=1., c=t)
    colorbar = fig.colorbar(mappable=pc, cax=fig.axes[1])
    colorbar.set_label('T', fontsize=16.)

    plt.close(fig)

    return fig
