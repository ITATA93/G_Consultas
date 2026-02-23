# SQLUser.SS_UserDepartFunction

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DF_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| DF_Childsub | double |  |  | NO | Childsub |
| DF_Column | varchar |  |  | SI | Column |
| DF_RowId | varchar |  |  | NO | - |
| DF_TableName | varchar |  |  | SI | TableName |
| DF_Width | varchar |  |  | SI | Column Width |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*