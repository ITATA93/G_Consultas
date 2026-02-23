# lab.CT_DoctorsInGroup

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDGD_ParRef | varchar | PK |  | NO | CT_DoctorGroup Parent Reference |
| CTDGD_Doctor_DR | varchar |  | FK | NO | Des Ref Doctor |
| CTDGD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*