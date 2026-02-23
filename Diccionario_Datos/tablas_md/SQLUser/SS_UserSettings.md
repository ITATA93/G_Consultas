# SQLUser.SS_UserSettings

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SET_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| SET_AppCode | varchar |  |  | SI | Application Code |
| SET_Childsub | double |  |  | NO | Childsub |
| SET_Key | varchar |  |  | SI | Key |
| SET_Parameter | varchar |  |  | SI | Parameter |
| SET_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*