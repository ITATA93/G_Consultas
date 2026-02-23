# SQLUser.PAC_MotherOutcome

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MTHROC_Code | varchar | PK |  | NO | Code |
| MTHROC_CodeTableTags | varchar | PK |  | SI | List of code table Tags |
| MTHROC_CreatedDate | date | PK |  | SI | Created Date |
| MTHROC_CreatedTime | time | PK |  | SI | Created Time |
| MTHROC_CreatedUser_DR | bigint | PK | FK | SI | Created User |
| MTHROC_DateFrom | date | PK |  | SI | Date From |
| MTHROC_DateTo | date | PK |  | SI | Date To |
| MTHROC_Desc | varchar | PK |  | NO | Description |
| MTHROC_Owner | varchar | PK |  | SI | Owner |
| MTHROC_RowId | bigint | PK |  | NO | - |
| MTHROC_UpdatedDate | date | PK |  | SI | Updated Date |
| MTHROC_UpdatedTime | time | PK |  | SI | Updated Time |
| MTHROC_UpdatedUser_DR | bigint | PK | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*