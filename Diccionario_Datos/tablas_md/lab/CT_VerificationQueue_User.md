# lab.CT_VerificationQueue_User

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTVQU_ParRef | varchar | PK |  | NO | CT_VerificationQueue Parent Reference |
| CTVQU_RowID | varchar |  |  | NO | - |
| CTVQU_User_DR | varchar |  | FK | NO | User DR |
| CTVQU_xxx2 | varchar |  |  | SI | Viewable |
| CTVQU_xxx3 | varchar |  |  | SI | Printable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*