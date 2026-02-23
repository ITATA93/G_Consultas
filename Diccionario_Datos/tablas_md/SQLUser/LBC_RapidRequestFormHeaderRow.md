# SQLUser.LBC_RapidRequestFormHeaderRow

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRRFHR_ParRef | bigint | PK |  | NO | Parent table |
| LBCRRFHR_Caption | varchar |  |  | NO | Caption	 |
| LBCRRFHR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRRFHR_Column | integer |  |  | SI | Column |
| LBCRRFHR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRRFHR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRRFHR_RowID | varchar |  |  | NO | - |
| LBCRRFHR_Sequence | integer |  |  | SI | Sequence |
| Q161Q1 | - |  |  | SI | Items |
| Q161Q10 | - |  |  | SI | No Aplica |
| Q161Q2 | - |  |  | SI | Otro |
| Q161Q3 | - |  |  | SI | Descripción del Item |
| Q161Q4 | - |  |  | SI | Fecha de Vencimiento |
| Q161Q5 | - |  |  | SI | Control de Viraje |
| Q161Q6 | - |  |  | SI | Comentarios |
| Q161Q7 | - |  |  | SI | N° de Lote |
| Q161Q8 | - |  |  | SI | N° de Serie |
| Q161Q9 | - |  |  | SI | Modelo |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*