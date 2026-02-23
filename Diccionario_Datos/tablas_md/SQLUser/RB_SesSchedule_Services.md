# SQLUser.RB_SesSchedule_Services

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_ParRef | varchar | PK |  | NO | RB_SesSchedule Parent Reference |
| SER_Childsub | double |  |  | NO | Childsub |
| SER_RBC_Service_DR | bigint |  | FK | SI | Des Ref RBC_Service |
| SER_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*