# SQLUser.SS_ProfileDocResRestrictions

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRES_ParRef | bigint | PK |  | NO | Parent table |
| DRES_CTCP_DR | varchar |  | FK | SI | Care Provider |
| DRES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRES_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| DRES_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| DRES_RBC_Eq_DR | bigint |  | FK | SI | Resource |
| DRES_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*