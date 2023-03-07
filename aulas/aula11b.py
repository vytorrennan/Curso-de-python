# to finalize the background color put a \033[m where you wanna finalize
print('\033[4;30;45mHello, World!')
print('\033[4;30;45mHello, World!\033[m')

# test with the 7 style
print('\033[0;33;44mHello, World!\033[m')
print('\033[7;33;44mHello, World!\033[m')