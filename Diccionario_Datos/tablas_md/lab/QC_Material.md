# lab.QC_Material

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCM_RowID | varchar | PK |  | NO | - |
| QCM_Code | varchar |  |  | NO | Material Code |
| QCM_Comments | varchar |  |  | SI | Comments |
| QCM_CurrentLot | varchar |  |  | SI | Current Lot Number |
| QCM_Levels | double |  |  | SI | Number of Levels |
| QCM_Name | varchar |  |  | SI | Material Description |
| QCM_NoOfPoints | double |  |  | SI | Number of Points |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*