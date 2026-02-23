# SQLUser.PAC_SnomedWordEquivalent

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOWE_RowId | bigint | PK |  | NO | - |
| Q22Q1 | - |  |  | SI | Body location |
| Q22Q2 | - |  |  | SI | Muscle lenght |
| Q22Q3 | - |  |  | SI | Shortened muscle |
| Q22Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOWE_CreatedDate | date |  |  | SI | Created Date |
| SNOWE_CreatedTime | time |  |  | SI | Created Time |
| SNOWE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOWE_UpdatedDate | date |  |  | SI | Updated Date |
| SNOWE_UpdatedTime | time |  |  | SI | Updated Time |
| SNOWE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SNOWE_WordBlock | varchar |  |  | SI | WordBlock |
| SNOWE_WordRole | varchar |  |  | SI | WordRole |
| SNOWE_WordText | varchar |  |  | SI | WordText |
| SNOWE_WordType | varchar |  |  | SI | WordType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*