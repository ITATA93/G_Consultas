# Tools_Upload_OrderSet.DocumentOrderSets

**Schema:** Tools_Upload_OrderSet
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSL_RowId | bigint | PK |  | NO | - |
| DateFrom | date |  |  | SI | active |
| DateTo | date |  |  | SI | - |
| LastGenDate | date |  |  | SI | - |
| LastGenStatus | varchar |  |  | SI | - |
| LastGenTime | time |  |  | SI | - |
| LinkedDocDR | bigint |  | FK | SI | Reference for an Vendor Doc |
| LinkedOrdSetDR | varchar |  | FK | SI | Reference for the linked OrderSet /
it needs to b... |
| LinkedOrdSetDateDR | varchar |  | FK | SI | Reference for the linked OrderSet-Version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*