# SQLUser.RBC_OutcomeOfAppointLocation

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | RBC_OutcomeOfAppoint Parent Reference |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOC_CreatedDate | date |  |  | SI | Created Date |
| LOC_CreatedTime | time |  |  | SI | Created Time |
| LOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOC_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_UpdatedDate | date |  |  | SI | Updated Date |
| LOC_UpdatedTime | time |  |  | SI | Updated Time |
| LOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*