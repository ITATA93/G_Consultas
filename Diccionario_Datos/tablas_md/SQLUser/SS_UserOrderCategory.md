# SQLUser.SS_UserOrderCategory

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCAT_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| ORCAT_Childsub | double |  |  | NO | Childsub |
| ORCAT_OrderCateg_DR | bigint |  | FK | NO | Des Ref to OrderCateg |
| ORCAT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*