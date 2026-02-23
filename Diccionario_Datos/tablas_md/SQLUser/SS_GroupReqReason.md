# SQLUser.SS_GroupReqReason

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REQR_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| REQR_Childsub | double |  |  | NO | Childsub |
| REQR_RequestReason_DR | bigint |  | FK | SI | Des Ref RequestReason |
| REQR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*