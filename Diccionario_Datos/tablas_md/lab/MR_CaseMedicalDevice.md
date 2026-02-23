# lab.MR_CaseMedicalDevice

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCMD_ParRef | varchar | PK |  | NO | MR_Case Parent Reference |
| MRCMD_MedicalDevice | varchar |  |  | SI | Medical Device |
| MRCMD_MedicalDeviceFT | varchar |  |  | SI | Medical Device Free Text |
| MRCMD_OrderNumber | double |  |  | NO | Order Number |
| MRCMD_Removed | varchar |  |  | SI | Removed |
| MRCMD_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*