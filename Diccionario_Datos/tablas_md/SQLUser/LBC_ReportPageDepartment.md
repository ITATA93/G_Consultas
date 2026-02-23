# SQLUser.LBC_ReportPageDepartment

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRPD_ParRef | bigint | PK |  | NO | - |
| LBCRPD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRPD_Department_DR | bigint |  | FK | NO | - |
| LBCRPD_RowID | varchar |  |  | NO | - |
| LBCRPD_UseTestItemAltCode | varchar |  |  | SI | Use Test Item Alternate Code in Report Body (Cumul... |
| LBCRPD_UseTestItemAltDesc | varchar |  |  | SI | Use Test Item Alternate Description in Report Body... |
| LBCRPD_UseTestSetAltDesc | varchar |  |  | SI | Use Test Set Alternate Description in Report Body ... |
| Q22Q1 | - |  |  | SI | Establecimiento De Tratamiento |
| Q22Q2 | - |  |  | SI | Área |
| Q22Q3 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*