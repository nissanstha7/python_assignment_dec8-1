#!/usr/bin/python3
v=25
u=0
t=10

print('We have,\n\tv = {} m/s\n\tu = {} m/s\n\tt = {} s'.format(v,u,t))

print('\tacceleration(a)=?\nNow,\n\t   v = u + at\n\t=> a = (v-u) / t')

acc=(v-u)/t
print('\t     = ({}-{}) / {}\n\t     = {}'.format(v,u,t,acc))

print('\nHence, acceleration = {} m/s\u00b2.'.format(acc))

print('Press enter key to exit...',end='')
input()
