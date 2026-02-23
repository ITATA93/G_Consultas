# SQLUser.LBDR_LegendEntry

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRLE_ParRef | bigint | PK |  | NO | The legend containing this entry |
| LBDRLE_Code | varchar |  |  | SI | Code
The code for the legend entry, e.g. "TF" |
| LBDRLE_Desc | varchar |  |  | SI | Description
The description for the legend entry,... |
| LBDRLE_DescDataType | varchar |  |  | SI | Desc DataType
The type of LBDRLEDesc
Can be "PT"... |
| LBDRLE_RowID | varchar |  |  | NO | - |
| LBDRLE_Seq | integer |  |  | SI | Sequence
Relationships are not ordered.  This ens... |
| Q03Q1 | - |  |  | SI | Fecha de Presentacion 1 |
| Q03Q2 | - |  |  | SI | Motivo de Rechazo |
| Q03Q3 | - |  |  | SI | Medicamento |
| Q03Q4 | - |  |  | SI | N° de Repetición |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*