import sapiens

best_1 = sapiens.predict_masked(
    'MTTPE*LKIHKEV*RAMDYLILMKHYYPEMTDEELKTPEMIEE*AKT*GNVDKK*F*ILFEIYGTTENI**AYYNGEM*PVVD*MVKLK',
    'H'
)

best_2 = sapiens.predict_masked(
    '***WER*SEEFVKMVEEKYGK**GELVREILKEVAEREFPDGKMSHREFRN*LYR*PFH*HHAAFKNPKY*SLITKFDPDELKEMAEKIP',
    'H'
)

print("\n")

print(best_1)

print("\n")

print(best_2)
