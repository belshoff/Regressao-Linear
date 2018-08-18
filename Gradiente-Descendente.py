
# coding: utf-8

# In[15]:


from matplotlib import pyplot as plt
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')


x_old, x_new, gamma, prec = 0, 6, 0.01, 0.00001

f = lambda x: x**4 - 3 * x**3 + 2
df = lambda x: 4*(x**3) - 9*(x**2)

to_plot =[]
i = 0

to_plot.append(x_new)
while abs(x_new - x_old) > prec:
    x_old = x_new
    x_new += -gamma * df(x_old)
    #to_plot.append(x_new)
    i += 1
    
    data = np.linspace(-10, 10, 10)
    plt.plot(data, f(data), 'b')
    to_plot.append(x_new)

plt.plot(to_plot, [f(x) for x in to_plot], 'r*')
plt.plot(to_plot, [f(x) for x in to_plot], 'g')
plt.show()
    

