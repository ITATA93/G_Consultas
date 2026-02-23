# SQLUser.LBC_SpecimenDepartment

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPDEP_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| LBCSPDEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPDEP_Department_DR | bigint |  | FK | SI | Department that use the Specimen Type |
| LBCSPDEP_RowID | varchar |  |  | NO | - |
| Q31Q1 | - |  |  | SI | Proxima Fecha |
| Q31Q2 | - |  |  | SI | Tipo Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*