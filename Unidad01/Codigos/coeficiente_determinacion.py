from sklearn.metrics import r2_score

r2 = r2_score(y, y_calculada)
print(f'Coeficiente de determinación: {r2:.2%}\n')
