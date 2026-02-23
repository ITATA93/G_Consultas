# SQLUser.SS_UserDefWinContRespAct

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACT_ParRef | varchar | PK |  | NO | SS_UserDefWinContResp Parent Reference |
| ACT_Childsub | double |  |  | NO | Childsub |
| ACT_Control_DR | varchar |  | FK | SI | Des Ref UsDefWinCont |
| ACT_RowId | varchar |  |  | NO | - |
| ACT_Score | varchar |  |  | SI | Score |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*