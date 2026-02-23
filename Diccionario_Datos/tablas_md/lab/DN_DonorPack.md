# lab.DN_DonorPack

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DNP_ParRef | varchar | PK |  | NO | DN_Donor Parent Reference |
| DNP_BBPack_DR | varchar |  | FK | NO | BBpack DR |
| DNP_Episode_DR | varchar |  | FK | NO | Episode DR |
| DNP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*