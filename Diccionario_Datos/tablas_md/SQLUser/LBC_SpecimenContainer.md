# SQLUser.LBC_SpecimenContainer

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPCON_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| ChildQControlDR | - |  |  | SI | Child Reference: Control |
| LBCSPCON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPCON_Container_DR | bigint |  | FK | SI |  Container that the Specimen Type can use |
| LBCSPCON_RowID | varchar |  |  | NO | - |
| QExaQ1 | - |  |  | SI | Examenes |
| QExaQ2 | - |  |  | SI | Fecha |
| QExaQ3 | - |  |  | SI | Resultado |
| QExaQ4 | - |  |  | SI | Examen Vigente |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*