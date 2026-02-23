# lab.PAD_DoctorsRequestPadsDoc

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PADDR_ParRef | varchar | PK |  | NO | PAD_DoctorsRequestPads Parent Reference |
| PADDR_Doctor_DR | varchar |  | FK | SI | Doctor DR |
| PADDR_Order | numeric |  |  | NO | Order number |
| PADDR_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*