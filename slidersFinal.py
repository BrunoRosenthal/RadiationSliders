import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def decay(Ap, Bp):
    A, B, C = 10 ** 5, 0, 0
    speciesA, speciesB, speciesC, time, total = [], [], [], [], []
    for t in range(10 ** 3):
        newA = A - A * Ap
        newB = (B + A * Ap) - ((B + A * Ap) * Bp)
        newC = C + ((B + A * Ap) * Bp)
        A = newA
        B = newB
        C = newC
        speciesA.append(A)
        speciesB.append(B)
        speciesC.append(C)
        time.append(t)
        total.append(A+B+C)
    return speciesA, speciesB, speciesC, time, total

def get_slider(event):
    a = sliderA.get()
    b = sliderB.get()
    animate(a, b)

root = tk.Tk()
root.title("Decay Chain Model")
sliderA = tk.Scale(root, from_=1, to=0, resolution=10**-5, command=get_slider, orient="horizontal", label="Lambda 1", length=600)
sliderB = tk.Scale(root, from_=1, to=0, resolution=10**-5, command=get_slider, orient="horizontal", label="Lambda 2", length=600)
sliderA.pack()
sliderB.pack()

lines = []
fig, ax = plt.subplots()

def animate(Ap, Bp):
    speciesA, speciesB, speciesC, time, total = decay(Ap, Bp)
    ax.clear()

    ax.set_xlim([0,10**3])
    ax.set_ylim([0, 10**5 +10**3])
   
    ax.plot(time, speciesA)
    ax.plot(time, speciesB)
    ax.plot(time, speciesC)
    ax.plot(time, total)
    fig.canvas.draw_idle()

line = FigureCanvasTkAgg(fig, root)
line.get_tk_widget().pack()
animate(0, 0)
root.mainloop()
