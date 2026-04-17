def with_block():
    """Check the functionality of with statement"""

    with open('abc.txt','w') as f:
        f.write('Jacob')
        f.write('\n')
        f.write('Jerry\n')
        f.write('Samira\n')

    print(f'Is file closed: {f.closed}')

with_block()