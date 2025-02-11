print((True or False) and True )
        # True        and  True
                # True

print(((True and False) and True) or (False or True))
        # False and  True
                # False           or True
                        # True
print(True or ((False and True) or ((True and False)and (True or False))))

        #  t            f                   # f           &          t
#           t           f           or                      f