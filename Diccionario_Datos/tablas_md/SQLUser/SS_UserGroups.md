# SQLUser.SS_UserGroups

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| GRP_Childsub | double |  |  | NO | Childsub |
| GRP_DateFrom | date |  |  | SI | Date From |
| GRP_DateTo | date |  |  | SI | Date To |
| GRP_Group_DR | bigint |  | FK | SI | Des Ref Group |
| GRP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*