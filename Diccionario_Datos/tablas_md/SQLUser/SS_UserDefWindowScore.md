# SQLUser.SS_UserDefWindowScore

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCORE_ParRef | bigint | PK |  | NO | SS_UserDefWindow Parent Reference |
| SCORE_Caption | varchar |  |  | SI | Caption |
| SCORE_Childsub | double |  |  | NO | Childsub |
| SCORE_RowId | varchar |  |  | NO | - |
| SCORE_ScoreFrom | varchar |  |  | SI | Score From |
| SCORE_ScoreTo | varchar |  |  | SI | ScoreTo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*