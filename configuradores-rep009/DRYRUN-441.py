#!/usr/bin/env python3
"""DRY-RUN BM-CONFIG REP-009. SOLO LECTURA: no abre red, no escribe en produccion.
Genera plan de cambios y rollback desde MATRIZ-441.csv (solo filas READY).
Ejecucion real: NO incluida; requiere autorizacion A4 expresa + backup PS fresco + control de concurrencia."""
import csv,sys,hashlib,datetime
m=list(csv.DictReader(open(sys.argv[1],encoding='utf-8-sig')))
ready=[x for x in m if x['estado']=='READY']
assert len(m)==441 and len({x['id_product_attribute'] for x in m})==441
plan=[(x['id_product_attribute'],x['SKU'],x['precio_actual_sin_iva'],x['precio_propuesto_sin_iva']) for x in ready]
# Control de concurrencia (a aplicar en ejecucion real): releer precio vivo por id_product_attribute;
# si != precio_actual del backup -> ABORTAR esa fila (no sobrescribir cambios ajenos). Lotes <=50, parada si 1 fallo.
with open(sys.argv[2],'w',newline='') as f:
    w=csv.writer(f);w.writerow(['id_product_attribute','sku','precio_actual','precio_propuesto','precondicion_precio_vivo_eq_actual'])
    for r in plan: w.writerow(list(r)+['VERIFICAR_EN_VIVO'])
with open(sys.argv[3],'w',newline='') as f:   # rollback = inverso exacto
    w=csv.writer(f);w.writerow(['id_product_attribute','sku','precio_a_restaurar'])
    for r in plan: w.writerow([r[0],r[1],r[2]])
print(len(plan),'filas READY;',hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest()[:16],datetime.date.today())
