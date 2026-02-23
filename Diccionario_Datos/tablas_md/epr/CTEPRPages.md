# epr.CTEPRPages

**Schema:** epr
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AllowAddition | bit |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| EditComponentDR | bigint |  | FK | SI | - |
| IsHistoryPage | bit |  |  | SI | - |
| ListComponentDR | bigint |  | FK | SI | - |
| Owner | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| URL | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*