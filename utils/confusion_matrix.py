"""2-class confusion matrix."""

def cm(y_true, y_pred):
    tp=fp=fn=tn=0
    for t,p in zip(y_true,y_pred):
        if t and p: tp+=1
        elif not t and p: fp+=1
        elif t and not p: fn+=1
        else: tn+=1
    return {'tp':tp,'fp':fp,'fn':fn,'tn':tn}
