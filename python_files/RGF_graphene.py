import numpy as np

def main():
	epsB = 0.
	epsA = 0.
	t = 1. 
	a = 1. 
	kx = 2*np.pi/a * 0.1 
	kxvals = np.linspace(0,2*np.pi/a,10)
	kxvals = (kx,)

	kwargs = {  't':t, 
				'a':a,
				'epsA': epsA,
				'epsB': epsB 
				}

	def ret_H0(kx,t,a,epsA,epsB):
		P = np.matrix([[0,0,0,-np.conj(t)*np.exp(-1j*kx*a)],[0,0,0,0],[0,0,0,0],[-t*np.exp(1j*kx*a),0,0,0]]) 
		M = np.matrix([[epsB,-np.conj(t),0,0],[-t,epsA,-t,0],[0,-np.conj(t),epsB,-t],[0,0,-np.conj(t),epsA]])
		return M + P

	Q = np.matrix([[0,-t,0,0],[-np.conj(t),0,0,0],[0,0,0,-np.conj(t)],[0,0,-t,0]])
	Ty = np.matrix([[0,-t,0,0],[0,0,0,0],[0,0,0,0],[0,0,-t,0]]) #Right hopping matrix along Y
	# H0 = ret_H0(kx,**kwargs)

	np.testing.assert_almost_equal(Q,Q.H)

	omega = 0.1
	G0invarr = [(omega - ret_H0(kx,**kwargs)).I for kx in kxvals]
	#G = np.linalg.inv(G0inv) #Initialize G to G0
	Garr = [G0inv.I for G0inv in G0invarr]
	#Garr = map(np.linalg.inv,G0invarr)
	itern = 10
	for i in range(itern):
		for i,G in enumerate(Garr):
			Garr[i] = np.linalg.inv(G0invarr[i] - Ty@G@Ty.H)
	print(Garr)


if __name__ == '__main__': 
	main()