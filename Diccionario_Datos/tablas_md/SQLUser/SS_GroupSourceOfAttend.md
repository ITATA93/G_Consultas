# SQLUser.SS_GroupSourceOfAttend

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SATT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SATT_Childsub | double |  |  | NO | Childsub |
| SATT_RowId | varchar |  |  | NO | - |
| SATT_SourceOfAttendance_DR | bigint |  | FK | SI | Des Ref SourceOfAttendance |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*