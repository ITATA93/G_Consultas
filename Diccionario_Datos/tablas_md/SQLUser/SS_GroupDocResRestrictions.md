# SQLUser.SS_GroupDocResRestrictions

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRES_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| DRES_CTCP_DR | varchar |  | FK | SI | Des REf CTCP_DR |
| DRES_Childsub | double |  |  | NO | Childsub |
| DRES_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| DRES_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| DRES_RBC_Eq_DR | bigint |  | FK | SI | Des Ref RBC Equip |
| DRES_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*