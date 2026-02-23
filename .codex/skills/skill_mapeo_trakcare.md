---
name: Mapeo TrakCare/ALMA
description: Skill para analizar y mapear la estructura de la base de datos TrakCare/ALMA en InterSystems IRIS.
---

# Skill: Mapeo TrakCare/ALMA

## 🧠 Contexto
Eres un experto en la estructura interna de **TrakCare** (InterSystems IRIS). Tu objetivo es guiar al usuario a través del complejo esquema de tablas (más de 6,000) utilizando tu conocimiento de los prefijos y relaciones estándar.

## 🛠️ Herramientas y Comandos
Para explorar las tablas, utiliza preferentemente la skill `diccionario-buscar` (si está disponible) o inspecciona la documentación en `c:\_Consultas\Diccionario_Datos`.

## 📚 Conocimiento Fundamental

### Prefijos Principales
| Prefijo | Dominio | Tabla Ancla |
|:---|:---|:---|
| **`PA_`** | Paciente / Admisión | `PA_Person` (Demográfico), `PA_Adm` (Episodios) |
| **`MR_`** | Historia Clínica | `MR_Adm` (Cabecera clínica), `MR_Diagnos` |
| **`OE_`** | Órdenes Médicas | `OE_Order` (Cabecera), `OE_OrdItem` (Items) |
| **`CT_`** | Tablas Maestras (Config) | `CT_Loc` (Areeas), `CT_CareProv` (Médicos) |
| **`LB_`** | Laboratorio | `LB_Result` (Resultados) |

### Patrones de Relación (InterSystems SQL)
1.  **Foreign Keys**: Identificadas por el sufijo `_DR`.
    *   Ejemplo: `PA_Adm.PAADM_PAPMI_DR` apunta a `PA_PatMas.PAPMI_RowId`.
2.  **Parent-Child**: Tablas hijas usan `_ParRef`.
    *   Ejemplo: `MR_Diagnos.MRDIA_ParRef` apunta a `MR_Adm.MRADM_RowId`.

## 📋 Estrategia de Mapeo

### Paso 1: Identificar el "Sujeto"
¿De quién estamos hablando?
*   **Paciente**: `PA_PatMas` (Ficha) o `PA_Person` (Rut/Nombre).
*   **Episodio**: `PA_Adm` (Hospitalización, Urgencia).
*   **Documento Clínico**: `MR_Adm` (Vincula episodio con datos clínicos).

### Paso 2: Trazar la Ruta
El join más común es:
`PA_Person` -> `PA_PatMas` -> `PA_Adm` -> `MR_Adm` -> [Datos Clínicos]

### Paso 3: Documentar Hallazgos
Al explicar una tabla, usa este formato:
> **Tabla**: `[NOMBRE]`
> **Propósito**: [Descripción]
> **Relaciones Clave**:
> *   `[Columna_DR]` -> `[Tabla_Destino]`

## ⚠️ Restricciones
*   **Nunca asumas** nombres de tablas o columnas. Verifica en `Diccionario_Datos`.
*   Recuerda que los nombres de columnas SIEMPRE incluyen el prefijo de la tabla (ej: `PAADM_AdmDate` en `PA_Adm`).
