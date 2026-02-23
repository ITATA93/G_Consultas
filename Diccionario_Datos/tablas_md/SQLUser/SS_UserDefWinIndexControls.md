# SQLUser.SS_UserDefWinIndexControls

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONT_ParRef | varchar | PK |  | NO | SS_UserDefWindowIndex Parent Reference |
| CONT_Childsub | double |  |  | NO | Childsub |
| CONT_Inactive | varchar |  |  | SI |  Inactive |
| CONT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| CONT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CONT_RowId | varchar |  |  | NO | - |
| CONT_UserDefWindowControls_DR | varchar |  | FK | SI | Des Ref SSUserDefWindowControls |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*