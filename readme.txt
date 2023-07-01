LHC is the code with the original architecture and LHC_nov is code with the changes in the architecture mostly in one file lib\LHC_net.py. No change in execution below.

1. Create conda env , install pip (please do this)
   > pip install -r requirements.txt
2. Copy the data folder into both folders LHC and LHC_nov
3. > python ETL.py
4. > python LHC_Net_Train.py > &1 | tee train_op.txt
5. > python LHC_Net_Eval.py > &1 | tee eval_op.txt

