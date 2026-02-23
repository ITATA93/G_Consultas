# lab.FI_FamilyIndexRecords

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FINDR_ParRef | varchar | PK |  | NO | FamilyIndex Parent Reference |
| FINDR_DateEnd | date |  |  | SI | Date End |
| FINDR_DateStart | date |  |  | SI | Date Start |
| FINDR_Patient | varchar |  |  | NO | Patient |
| FINDR_Relations | varchar |  |  | SI | Relations |
| FINDR_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*