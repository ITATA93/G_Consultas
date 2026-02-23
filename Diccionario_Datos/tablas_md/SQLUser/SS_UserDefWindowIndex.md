# SQLUser.SS_UserDefWindowIndex

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IND_ParREf | bigint | PK |  | NO | SS_UserDefWindow Parent Reference |
| IND_Childsub | double |  |  | NO | Childsub |
| IND_Inactive | varchar |  |  | SI | Inactive |
| IND_IndexName | varchar |  |  | SI | IndexName |
| IND_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| IND_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| IND_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*