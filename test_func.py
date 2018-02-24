def setup(ncar,nbox):
    curtains=[]
    for i in range(ncar):
        curtains.append("car")
    ngoat=nbox - ncar  
    for i in range(ngoat):
        curtains.append("goat")
    return random.sample(curtains, len(curtains))
def lets_play_a_game(ncar,nbox,switch):
    curtains_pls=setup(ncar,nbox)
    guess=np.random.choice(nbox)
    if switch==0:
        
        if curtains_pls[guess]=='car':
            return 1
        else:
            return 0
    for w in range(nbox):
        if curtains_pls[w]=="car":
            idx_ans=w
            
    arr_reveal=np.arange(nbox)
    if idx_ans!=guess:
        arr_reveal=np.delete(arr_reveal,[guess,idx_ans])
    else:
        arr_reveal=np.delete(arr_reveal,guess)
    
    reveal=np.random.choice(arr_reveal,switch)
    
    
    arr_final=list(np.arange(nbox))
    arr_final=np.delete(arr_final,[reveal,guess])
    result=np.random.choice(arr_final,1)
    
    if curtains_pls[result]=='car':
        return 1
    else:
        return 0
def iter_test(ncar,nbox,iters,switch):
    tally=0
    for i in range(iters):
        tally+=lets_play_a_game(ncar,nbox,switch)
    return tally/iters
