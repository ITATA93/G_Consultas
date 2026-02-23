# SQLUser.RB_EventTimesConflicts

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ECONF_ParRef | varchar | PK |  | NO | RB_EventTimes Parent Reference |
| ECONF_CareProv_DR | varchar |  | FK | SI | Care Provider ID |
| ECONF_Childsub | double |  |  | NO | Childsub |
| ECONF_Desc | varchar |  |  | SI | Description |
| ECONF_PatMas_DR | bigint |  | FK | SI | Patient ID |
| ECONF_RowId | varchar |  |  | NO | - |
| ECONF_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*