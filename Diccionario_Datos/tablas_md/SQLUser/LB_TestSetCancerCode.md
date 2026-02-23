# SQLUser.LB_TestSetCancerCode

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSCC_ParRef | bigint | PK |  | NO | - |
| LBTSCC_CancerCode_DR | bigint |  | FK | SI | - |
| LBTSCC_RowID | varchar |  |  | NO | - |
| LBTSCC_Value | varchar |  |  | SI | - |
| QControlQ1 | - |  |  | SI | Fecha Tentativa Proximo Control |
| QControlQ2 | - |  |  | SI | Tipo Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*