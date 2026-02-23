# SQLUser.LB_TransferSpecimenContainer

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTRSPC_ParRef | bigint | PK |  | NO | Parent Reference |
| LBTRSPC_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material DR |
| LBTRSPC_Received | varchar |  |  | SI | Received |
| LBTRSPC_RowID | varchar |  |  | NO | - |
| LBTRSPC_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container DR |
| Q29Q1 | - |  |  | SI | Categoria |
| Q29Q2 | - |  |  | SI | Sustancia |
| Q29Q3 | - |  |  | SI | Frecuencia |
| Q29Q4 | - |  |  | SI | Edad de Inicio |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*