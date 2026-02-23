# SQLUser.SS_UserDefWinGroup

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WINGRP_RowId | bigint | PK |  | NO | - |
| WINGRP_Code | varchar |  |  | NO | Code |
| WINGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WINGRP_Desc | varchar |  |  | NO | Description |
| WINGRP_Owner | varchar |  |  | SI | Owner |
| WINGRP_Purpose | varchar |  |  | SI | Purpose |
| WINGRP_QuestAdmRestrict | varchar |  |  | SI | QuestAdmRestrict |
| WINGRP_QuestReadOnly | varchar |  |  | SI | QuestReadOnly |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*