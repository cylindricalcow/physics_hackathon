
import numpy as np
import matplotlib.pyplot as plt

def readmesh(fname):
    """
    Read a mesh file and return vertices as a (npts, 2)
    numpy array and triangles as (ntriangles, 3) numpy
    array. `npts` is the number of vertices of the mesh
    and `ntriangles` is the number of triangles of the
    mesh.
    """

    with open(fname, "r") as f:
        npoints = int(next(f))
        points = np.zeros((npoints, 2))
        for i in range(npoints):
            points[i, :] = [float(x) for x in next(f).split()]

        ntriangles = int(next(f))
        triangles = np.zeros((ntriangles, 3), dtype=int)
        for i in range(ntriangles):
            triangles[i, :] = [int(x) - 1 for x in next(f).split()]

    return points, triangles


def plotmesh(points, triangles, tricolors=None):
    """
    Given a list of points (shape: (npts, 2)) and triangles
    (shape: (ntriangles, 3)), plot the mesh.
    """

    plt.figure()
    plt.gca().set_aspect('equal')
    if tricolors is None:
        plt.triplot(points[:, 0], points[:, 1], triangles, 'bo-', lw=1.0)
    else:
        plt.tripcolor(points[:, 0], points[:, 1], triangles,
                      facecolors=tricolors, edgecolors='k')
    plt.show()
    return