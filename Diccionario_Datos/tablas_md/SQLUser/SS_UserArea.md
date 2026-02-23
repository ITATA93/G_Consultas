# SQLUser.SS_UserArea

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AR_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| AR_Area_DR | bigint |  | FK | SI | Des Ref Area |
| AR_Childsub | double |  |  | NO | Childsub |
| AR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*