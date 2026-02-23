# lab.CT_SpecimenGroupItems

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSGI_ParRef | varchar | PK |  | NO | CT_SpecimeGroup Parent Reference |
| CTSGI_RowID | varchar |  |  | NO | - |
| CTSGI_Specimen_DR | varchar |  | FK | NO | Specimen DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*