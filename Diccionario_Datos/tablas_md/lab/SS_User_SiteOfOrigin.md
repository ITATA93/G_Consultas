# lab.SS_User_SiteOfOrigin

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUSO_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUSO_DBLab_DR | varchar |  | FK | NO | DB Laboratory DR |
| SUSO_RowID | varchar |  |  | NO | - |
| SUSO_SiteOfOrigin_DR | varchar |  | FK | SI | Site of Origin DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*